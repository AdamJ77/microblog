import React from "react";
import Posts from "../components/home/Posts";
import LeftBar from "../components/home/LeftBar";
import MainSection from "../components/home/MainSection";

export default function Home() {
  return (
    <div style={{ display: "flex" }}>
      <LeftBar />
      <MainSection />
    </div>
  );
}
