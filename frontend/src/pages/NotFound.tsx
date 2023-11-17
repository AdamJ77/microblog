import React, { CSSProperties } from "react";
import NotFoundInfo from "../components/notFound/NotFoundInfo";

export default function NotFound() {
  const wraperStyles: CSSProperties = {
    backgroundColor: "var(--primary-color)",
    width: "100%",
    height: "100vh",
  };

  return (
    <div style={wraperStyles}>
      <NotFoundInfo />
    </div>
  );
}
