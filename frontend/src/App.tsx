import React, { lazy, Suspense, CSSProperties } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Loading from "./components/common/Loading";
import "react-photo-view/dist/react-photo-view.css";
import AuthContextProvider from "./context/AuthContext";
import { useAppContext } from "./context/AppContext";

const Home = lazy(() => import("./pages/Home"));
const Profile = lazy(() => import("./pages/Profile"));
const NotFound = lazy(() => import("./pages/NotFound"));
const Login = lazy(() => import("./pages/Login"));
const Signup = lazy(() => import("./pages/Signup"));

export default function App() {
  const { isLoading } = useAppContext();

  if (isLoading) {
    return <Loading text="" />;
  }

  const SuspenseWrapper = ({
    lazyComponent,
  }: {
    lazyComponent: React.LazyExoticComponent<() => JSX.Element>;
  }) => {
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
        {React.createElement(lazyComponent)}
      </Suspense>
    );
  };

  const authorize = (
    Component: React.LazyExoticComponent<() => JSX.Element>
  ) => {
    const suspenseStyles: CSSProperties = {
      width: "100%",
      height: "100vh",
      backgroundColor: "var(--primary-color)",
    };

    return (
      <AuthContextProvider>
        <Suspense
          fallback={
            <div style={suspenseStyles}>
              <Loading text="" />
            </div>
          }
        >
          <Component />
        </Suspense>
      </AuthContextProvider>
    );
  };

  const protectedRoutes = [
    {
      path: "/",
      component: Home,
    },
    {
      path: "/profile",
      component: Profile,
    },
  ];

  const routes = [
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
        {protectedRoutes.map((route, index) => (
          <Route
            key={index}
            path={route.path}
            element={authorize(route.component)}
          />
        ))}
        {routes.map((route, index) => (
          <Route
            key={index}
            path={route.path}
            element={<SuspenseWrapper lazyComponent={route.component} />}
          />
        ))}
      </Routes>
    </Router>
  );
}
