<template>
    <div id="entry">
        <h1>New entry</h1>
        <div class="form-inputs">
            <label for="height">Height</label>
            <input type="text" id="height" name="height" placeholder="in cm" />
        </div>
        <div class="form-inputs">
            <label for="water">Water Usage</label>
            <input type="text" id="water" name="water" placeholder="in litres" />
        </div>
        <div class="form-inputs">
            <label for="fert">Fetilizer Usage</label>
            <input type="text" id="fert" name="fert"  placeholder="in kg" />
        </div>
        <div class="form-inputs">
            <label for="date"></label>
            <input type="date" id="date" name="date"  placeholder="dd/mm/yy" />
        </div>
        <div>
    <router-link
      to="/MoreInfo"
      custom
      v-slot="{ navigate }"
    >
      <button
        @click="navigate"
        role="link"
      >
        Add new entry
      </button>
    </router-link>
  </div>
    </div>
</template>