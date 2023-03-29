<template>
    <div class="container-fluid py-4">
      <div class="row mb-4">
        <div class="col-lg-8 col-md-6 mb-md-0 mb-4">
          <div class="card">
            <div class="card-header pb-0">
              <div class="row">
                <div class="col-lg-6 col-7">
                  <h6>Inventory Management</h6>
                </div>
                <div class="col-lg-6 col-5 my-auto text-end">
                  <div class="dropdown float-lg-end pe-4">
                    <router-link to="/Entry">New Entry</router-link>
                  </div>
                </div>
              </div>
            </div>
            <div class="card-body px-0 pb-2">
              <div class="table-responsive">
                <table class="table align-items-center mb-0">
                  <thead>
                    <tr>
                      <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">ID</th>
                      <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2">Harvest Type</th>
                      <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">Weight</th>
                      <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">Expiry</th>
                      <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">options</th>

                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <div class="d-flex px-2 py-1">
                          <div class="d-flex flex-column justify-content-center">
                            <h6 class="mb-0 text-sm">1</h6>
                          </div>
                        </div>
                      </td>
                      <td>
                        <span class="text-xs font-weight-bold">Wheat</span>
                      </td>
                      <td class="align-middle text-center text-sm">
                        <span class="text-xs font-weight-bold"> 20 KG </span>
                      </td>
                      <td class="align-middle">
                        <div class="progress-wrapper w-75 mx-auto">
                          <div class="progress-info">
                            <div class="progress-percentage text-center">
                              <span class="text-xs font-weight-bold">11-11-2023</span>
                            </div>
                          </div>
                        </div>
                      </td>
                      <td class="align-middle text-center"><router-link to="/Entry">Edit Entry</router-link></td>
                    </tr>
                    <tr>
                      <td>
                        <div class="d-flex px-2 py-1">
                          <div class="d-flex flex-column justify-content-center">
                            <h6 class="mb-0 text-sm">2</h6>
                          </div>
                        </div>
                      </td>
                      <td>
                        <span class="text-xs font-weight-bold">Wheat</span>
                      </td>
                      <td class="align-middle text-center text-sm">
                        <span class="text-xs font-weight-bold"> 20 KG </span>
                      </td>
                      <td class="align-middle">
                        <div class="progress-wrapper w-75 mx-auto">
                          <div class="progress-info">
                            <div class="progress-percentage text-center">
                              <span class="text-xs font-weight-bold">11-11-2023</span>
                            </div>
                          </div>
                        </div>
                      </td>
                      <td class="align-middle text-center"><router-link to="/Entry">Edit Entry</router-link></td>
                    </tr>
                    <tr>
                      <td>
                        <div class="d-flex px-2 py-1">
                          <div class="d-flex flex-column justify-content-center">
                            <h6 class="mb-0 text-sm">2</h6>
                          </div>
                        </div>
                      </td>
                      <td>
                        <span class="text-xs font-weight-bold">Wheat</span>
                      </td>
                      <td class="align-middle text-center text-sm">
                        <span class="text-xs font-weight-bold"> 20 KG </span>
                      </td>
                      <td class="align-middle">
                        <div class="progress-wrapper w-75 mx-auto">
                          <div class="progress-info">
                            <div class="progress-percentage text-center">
                              <span class="text-xs font-weight-bold">11-11-2023</span>
                            </div>
                          </div>
                        </div>
                      </td>
                      <td class="align-middle text-center"><router-link to="/Entry">Edit Entry</router-link></td>
                    </tr>
                    <tr>
                      <td>
                        <div class="d-flex px-2 py-1">
                          <div class="d-flex flex-column justify-content-center">
                            <h6 class="mb-0 text-sm">2</h6>
                          </div>
                        </div>
                      </td>
                      <td>
                        <span class="text-xs font-weight-bold">Wheat</span>
                      </td>
                      <td class="align-middle text-center text-sm">
                        <span class="text-xs font-weight-bold"> 20 KG </span>
                      </td>
                      <td class="align-middle">
                        <div class="progress-wrapper w-75 mx-auto">
                          <div class="progress-info">
                            <div class="progress-percentage text-center">
                              <span class="text-xs font-weight-bold">11-11-2023</span>
                            </div>
                          </div>
                        </div>
                      </td>
                      <td class="align-middle text-center"><router-link to="/Entry">Edit Entry</router-link></td>
                    </tr>
                    
                    <tr>
                      <td>
                        <div class="d-flex px-2 py-1">
                          <div class="d-flex flex-column justify-content-center">
                            <h6 class="mb-0 text-sm">2</h6>
                          </div>
                        </div>
                      </td>
                      <td>
                        <span class="text-xs font-weight-bold">Wheat</span>
                      </td>
                      <td class="align-middle text-center text-sm">
                        <span class="text-xs font-weight-bold"> 20 KG </span>
                      </td>
                      <td class="align-middle">
                        <div class="progress-wrapper w-75 mx-auto">
                          <div class="progress-info text-center">
                              <span class="text-xs font-weight-bold text-left">11-11-2023</span>
                          </div>
                        </div>
                      </td>
                      <td class="align-middle text-center"><router-link to="/Entry">Edit Entry</router-link></td>
                    </tr> 
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-md-6">
          <div class="card h-100">
            <div class="card-header pb-0">
              <h6>Orders overview</h6>
              <p class="text-sm">
                <i class="fa fa-arrow-up text-success" aria-hidden="true"></i>
                <span class="font-weight-bold">24%</span> this month
              </p>
            </div>
            <div class="card-body p-3">
              <div class="timeline timeline-one-side">
                <div class="timeline-block mb-3">
                  <span class="timeline-step">
                    <i class="material-icons text-success text-gradient">notifications</i>
                  </span>
                  <div class="timeline-content">
                    <h6 class="text-dark text-sm font-weight-bold mb-0">$2400, Design changes</h6>
                    <p class="text-secondary font-weight-bold text-xs mt-1 mb-0">22 DEC 7:20 PM</p>
                  </div>
                </div>
                <div class="timeline-block mb-3">
                  <span class="timeline-step">
                    <i class="material-icons text-danger text-gradient">code</i>
                  </span>
                  <div class="timeline-content">
                    <h6 class="text-dark text-sm font-weight-bold mb-0">New order #1832412</h6>
                    <p class="text-secondary font-weight-bold text-xs mt-1 mb-0">21 DEC 11 PM</p>
                  </div>
                </div>
                <div class="timeline-block mb-3">
                  <span class="timeline-step">
                    <i class="material-icons text-info text-gradient">shopping_cart</i>
                  </span>
                  <div class="timeline-content">
                    <h6 class="text-dark text-sm font-weight-bold mb-0">Server payments for April</h6>
                    <p class="text-secondary font-weight-bold text-xs mt-1 mb-0">21 DEC 9:34 PM</p>
                  </div>
                </div>
                <div class="timeline-block mb-3">
                  <span class="timeline-step">
                    <i class="material-icons text-warning text-gradient">credit_card</i>
                  </span>
                  <div class="timeline-content">
                    <h6 class="text-dark text-sm font-weight-bold mb-0">New card added for order #4395133</h6>
                    <p class="text-secondary font-weight-bold text-xs mt-1 mb-0">20 DEC 2:20 AM</p>
                  </div>
                </div>
                <div class="timeline-block mb-3">
                  <span class="timeline-step">
                    <i class="material-icons text-primary text-gradient">key</i>
                  </span>
                  <div class="timeline-content">
                    <h6 class="text-dark text-sm font-weight-bold mb-0">Unlock packages for development</h6>
                    <p class="text-secondary font-weight-bold text-xs mt-1 mb-0">18 DEC 4:54 AM</p>
                  </div>
                </div>
                <div class="timeline-block">
                  <span class="timeline-step">
                    <i class="material-icons text-dark text-gradient">payments</i>
                  </span>
                  <div class="timeline-content">
                    <h6 class="text-dark text-sm font-weight-bold mb-0">New order #9583120</h6>
                    <p class="text-secondary font-weight-bold text-xs mt-1 mb-0">17 DEC</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>
