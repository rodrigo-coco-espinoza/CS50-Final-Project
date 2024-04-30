import { combineReducers } from "redux";
import { auth } from './auth'
import { institucion_reducer } from "./pc_isla";

export default combineReducers({
    auth,
    institucion_reducer
})  