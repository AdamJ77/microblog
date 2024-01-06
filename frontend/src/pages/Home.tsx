import React from "react";
import LeftBar from "../components/home/LeftBar/LeftBar";
import MainSection from "../components/home/Main/MainSection";
import RightBar from "../components/home/RightBar/RightBar";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import HomePageContextProvider, {
  useHomePageContext,
} from "../context/HomePageContext";
import Loading from "../components/common/Loading";

function HomeInner() {
  const { isLoading } = useHomePageContext();
  const navigate = useNavigate();

  const handleLogout = async () => {
    await axios.post(
      `${process.env.REACT_APP_SERVER_URL}/auth/logout`,
      {},
      {
        withCredentials: true,
      }
    );

    navigate("/login");
  };

  if (isLoading) return <Loading text="" />;

  return (
    <>
      {/* <button onClick={handleLogout}>logout</button> */}
      <div style={{ display: "flex" }}>
        <LeftBar />
        <MainSection />
        <RightBar />
      </div>
    </>
  );
}

export default function Home() {
  return (
    <HomePageContextProvider>
      <HomeInner />
    </HomePageContextProvider>
  );
}
