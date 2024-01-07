import React from "react";
import LeftBar from "../components/home/LeftBar/LeftBar";
import MainSection from "../components/home/Main/MainSection";
import RightBar from "../components/home/RightBar/RightBar";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useAppContext } from "../context/AppContext";
import useCheckToken from "../hooks/useCheckToken";

export default function Home() {
  useCheckToken();
  const { tokenRef } = useAppContext();
  const navigate = useNavigate();

  const handleLogout = async () => {
    await axios.post(
      `${process.env.REACT_APP_SERVER_URL}/auth/logout`,
      {},
      {
        headers: {
          Authorization: `Bearer ${tokenRef.current}`,
        },
      }
    );

    tokenRef.current = null;
    navigate("/login");
  };

  return (
    <div style={{ display: "flex" }}>
      <LeftBar />
      <MainSection />
      <RightBar />
    </div>
  );
}
