const express = require("express");
const { graphqlHTTP } = require("express-graphql");
const { buildSchema } = require("graphql");
const axios = require("axios");

const app = express();

const schema = buildSchema(`
  type Query {
    manager(name: String!): ManagerResponse
  }

  type ManagerResponse {
    code: Int!
    ongrowingCrops: Int!
    inventory: Int!
    purchaseActivity: Int!
    totalCrop: Int!
  }

  
`);

// Root resolver
const root = {
  manager: async ({ name }) => {
    console.log(name);
    try {
      const inventoryResponse = await axios.get(
        `http://localhost:5000/inventory/${name}`
      );
      const currentInventory = inventoryResponse.data.data.quantity;

      const purchaseActivity = 0;

      const cropManagementResponse = await axios.get(
        `http://localhost:5001/crop_management/${name}`
      );
      const ongrowingCrops = cropManagementResponse.data.data;
      
      const numberOfOnGrowingCrops = ongrowingCrops.length;

      let totalCropsGrown =
        purchaseActivity - numberOfOnGrowingCrops - currentInventory;
      if (totalCropsGrown < 0) {
        totalCropsGrown = 0;
      }

      return {
        code: 200,
        ongrowingCrops: numberOfOnGrowingCrops,
        inventory: currentInventory,
        purchaseActivity: purchaseActivity,
        totalCrop: totalCropsGrown,
      };
    } catch (error) {
      console.error(error);
      return {
        code: 404,
        message:
          "There is an error accessing the Inventory Manager microservice.",
      };
    }
  },
};

// GraphQL endpoint
app.use(
  "/graphql",
  graphqlHTTP({
    schema,
    rootValue: root,
    graphiql: true,
  })
);

// Start the server
app.listen(5010, () => {
  console.log("Server started on port 5010");
});
