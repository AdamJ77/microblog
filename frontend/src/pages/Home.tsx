import React from "react";
import LeftBar from "../components/home/LeftBar/LeftBar";
import MainSection from "../components/home/Main/MainSection";
import RightBar from "../components/home/RightBar/RightBar";

export default function Home() {
  fetch(`${process.env.REACT_APP_SERVER_URL}/login/test`, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
    // credentials: "include",
  })
    .then((res) => res.json())
    .then((data) => console.log(data))
    .catch((err) => console.error(err));

  return (
    <div style={{ display: "flex" }}>
      <LeftBar />
      <MainSection />
      <RightBar />
    </div>
  );
}
