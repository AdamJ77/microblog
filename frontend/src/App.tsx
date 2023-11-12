import React, { lazy, Suspense, ComponentType } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Loading from "./components/common/Loading";
import "react-photo-view/dist/react-photo-view.css";

const Home = lazy(() => import("./pages/Home"));
const NotFound = lazy(() => import("./pages/NotFound"));

export default function App() {
  const suspensify = (Component: ComponentType) => {
    return (
      <Suspense fallback={<Loading text="" />}>
        <Component />
      </Suspense>
    );
  };

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
          <Route
            key={index}
            path={route.path}
            element={suspensify(route.component)}
          />
        ))}
      </Routes>
    </Router>
  );
}
