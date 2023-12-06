import React, { lazy, Suspense, ComponentType, CSSProperties } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Loading from "./components/common/Loading";
import "react-photo-view/dist/react-photo-view.css";

const Home = lazy(() => import("./pages/Home"));
const NotFound = lazy(() => import("./pages/NotFound"));
const Login = lazy(() => import("./pages/Login"));
const Signup = lazy(() => import("./pages/Signup"));

export default function App() {
  const suspensify = (Component: ComponentType) => {
    const suspenseStyles: CSSProperties = {
      width: "100%",
      height: "100vh",
      backgroundColor: "var(--primary-color)",
    };

    return (
      <Suspense
        fallback={
          <div style={suspenseStyles}>
            <Loading text="" />
          </div>
        }
      >
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
      path: "/login",
      component: Login,
    },
    {
      path: "/signup",
      component: Signup,
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
