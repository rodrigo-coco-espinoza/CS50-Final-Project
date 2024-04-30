import Error404 from "containers/errors/Error404";
import Home from "containers/pages/Home";
import { BrowserRouter as Router, Route, Routes, useLocation } from "react-router-dom";
import store from "store";
import { Provider } from "react-redux";
import { Helmet, HelmetProvider } from "react-helmet-async";
import AnimatedRoutes from "Routes";

function App() {
  
  return (
    <HelmetProvider>
      <Helmet>
        <title>CS50 | Final Project</title>
      </Helmet>
      <Provider store={store}>
        <Router>
          <AnimatedRoutes />         
        </Router>
      </Provider>
    </HelmetProvider>
    );
}

export default App;
