import React, { CSSProperties } from "react";
import SignupForm from "../components/signup/SignupForm";

export default function Signup() {
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
      <SignupForm />
    </div>
  );
}
