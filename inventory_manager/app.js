const express = require("express");
const { graphqlHTTP } = require("express-graphql");
const { buildSchema } = require("graphql");
const axios = require("axios");
const cors = require("cors");

const app = express();
app.use(cors());

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
    let currentInventory = 0;
    let purchaseActivity = 0;
    let numberOfOnGrowingCrops = 0;
    let totalCropsGrown = 0;

    try {
      const inventoryResponse = await axios.get(
        `http://inventory:5000/inventory/${name}`
      );
      currentInventory = inventoryResponse.data.data.quantity;
    } catch (error) {
      console.error(error);
    }

    try {
      const purchaseResponse = await axios.get(
        `http://purchase_activity:5006/purchase_request/${name}`
      );
      purchaseActivity = purchaseResponse.data["Total Sales"];
    } catch (error) {
      console.error(error);
    }

    try {
      const cropManagementResponse = await axios.get(
        `http://crop_management:5001/crop_management/${name}`
      );
      const ongrowingCrops = cropManagementResponse.data.data;
      numberOfOnGrowingCrops = ongrowingCrops.length;
    } catch (error) {
      console.error(error);
    }

    totalCropsGrown =
      purchaseActivity - numberOfOnGrowingCrops - currentInventory;
    if (totalCropsGrown < 0) {
      totalCropsGrown = 0;
    }

    return {
      code: 200,
      ongrowingCrops: numberOfOnGrowingCrops || 0,
      inventory: currentInventory || 0,
      purchaseActivity: purchaseActivity || 0,
      totalCrop: totalCropsGrown,
    };
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
