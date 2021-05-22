import building_json from "../../../json/building.json";
import APISRV from "../../../utils/apiserver";

const API_BUILDING = "/api/building/";

function handleErrorsWithMock(response, mock_json) {
  if (!response.ok) {
    if (mock_json) {
      return mock_json;
    }
    throw Error(response.statusText);
  }
  return response.json();
}

var myHeaders = new Headers({ "content-type": "application/json" });
var myInit = { method: "GET", headers: myHeaders };

const state = {
  building_elevators: [""],
  building_elevators_network_error: "OK",
  hello: "hello people"
};

const mutations = {
  UPDATE_BUILDINGELEVATORS(state, payload) {
    state.building_elevators = payload;
  },
  UPDATE_BUILDINGELEVATORS_NETWORK_ERROR(state, payload) {
    state.building_elevators_network_error = payload;
  }
};

const actions = {
  getBuildingElevators({ commit }) {
    const url = APISRV + API_BUILDING;
    console.log("getBuildingElevators fetch", myInit, myHeaders, url);
    fetch(url, {
      method: "GET",
      mode: "no-cors",
      headers: {
        "Content-Type": "applications/json"
      }
    })
      .then((response) => {
        console.log("then", response);
        if (!response.ok) {
          throw Error(response.statusText);
        }
        console.log(response, response.json());
        return response.json();
      })
      .then((data) => {
        console.log("data", data);
        commit("UPDATE_BUILDINGELEVATORS", data);
        if (state.building_elevators_network_error != "OK") {
          commit("UPDATE_BUILDINGELEVATORS_NETWORK_ERROR", "OK");
        }
      })
      .catch((error) => {
        console.log("UPDATE_BUILDINGELEVATORS_NETWORK_ERROR", error);
        // weird
        // so we keep it for later
        if (error != "Error") {
          commit("UPDATE_BUILDINGELEVATORS_NETWORK_ERROR", error + " " + url);
          commit("UPDATE_BUILDINGELEVATORS", building_json);
        }
      });
  }
};

const getters = {
  building_elevators: (state) => state.building_elevators,
  building_elevators_network_error: (state) => state.building_elevators_network_error,
  hello: (state) => state.people
};

export default {
  state,
  mutations,
  actions,
  getters
};
