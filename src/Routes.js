import { BrowserRouter as Router, Route, Routes, useLocation } from "react-router-dom";
import Error404 from "containers/errors/Error404";
import Home from "containers/pages/Home";
import { AnimatePresence } from "framer-motion";
import User from "containers/pages/User";
import PcIsla from "containers/pages/PcIsla";

function AnimatedRoutes(){
    const location = useLocation()
    return(
        <AnimatePresence>
          <Routes location={location} key={location.pathname}>
            {/* Error display */}
            <Route path="*" element={<Error404 />} />
            {/* Home display */}
            <Route path="/" element={<Home />} />
            {/* PC Isla */}
            <Route path="/pc_isla" element={<PcIsla />} />
            {/* Login usuarios */}
            <Route path="/usuarios" element={<User />} />

          </Routes>
        </AnimatePresence>
    )
}

export default AnimatedRoutes