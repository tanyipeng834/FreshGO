<template>
  <form>
    <div class="form-group">
      <label for="date">Input harvest date: </label>
      <input type="date" id="date" name="date"  placeholder="dd/mm/yy" />
  </div>
  <div class="form-group">
    <label for="height">Height</label>
    <input type="text" class="form-control" id="height" aria-describedby="emailHelp" placeholder="Height in Metres">
  </div>
  
  <div class="form-group">
    <label for="water">Water Usage</label>
    <input type="number" class="form-control" id="water" placeholder="Amount in Litres">
  </div>
  <div class="form-group">
    <label for="fertilizer">Fertilizer Usage</label>
    <input type="number" class="form-control" id="fertilizer" placeholder="fertilizer in KG">
  </div>
    <button type="submit" class="btn btn-secondary" style="float:right">Cancel</button>
    <button type="submit" class="btn btn-primary" style="float:right">Add Entry</button>
    
  </form>
</template>

