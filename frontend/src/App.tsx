import React from "react";
import Home from "./pages/Home";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NotFound from "./pages/NotFound";

export default function App() {
  const routes = [
    {
      path: "/",
      component: Home,
    },
    {
      path: "*",
      component: NotFound,
    },
  ];
  return (
    <Router>
      <Routes>
        {routes.map((route, index) => (
          <Route key={index} path={route.path} Component={route.component} />
        ))}
      </Routes>
    </Router>
  );
}
