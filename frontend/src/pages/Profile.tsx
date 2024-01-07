import React from "react";
import useCheckToken from "../hooks/useCheckToken";

export default function Profile() {
  useCheckToken();

  return <div>Profile</div>;
}
