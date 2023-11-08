import React from "react";
import LeftBar from "../components/home/LeftBar/LeftBar";
import MainSection from "../components/home/Main/MainSection";
import RightBar from "../components/home/RightBar/RightBar";

export default function Home() {
  return (
    <div style={{ display: "flex" }}>
      <LeftBar />
      <MainSection />
      <RightBar />
    </div>
  );
}
