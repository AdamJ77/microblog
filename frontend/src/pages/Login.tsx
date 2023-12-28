import React, { CSSProperties } from "react";
import LoginForm from "../components/login/LoginForm";

export default function Login() {
  const wrapperStyles: CSSProperties = {
    backgroundImage: `url(${process.env.PUBLIC_URL}/images/login_background.png)`,
    backgroundRepeat: "no-repeat",
    backgroundSize: "cover",
    backgroundPosition: "center center",
    width: "100%",
    height: "100vh",
  };

  return (
    <div style={wrapperStyles}>
      <LoginForm />
    </div>
  );
}
