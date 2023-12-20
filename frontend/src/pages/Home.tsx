import React, { startTransition, useEffect } from "react";
import LeftBar from "../components/home/LeftBar/LeftBar";
import MainSection from "../components/home/Main/MainSection";
import RightBar from "../components/home/RightBar/RightBar";
import { useNavigate } from "react-router-dom";

export default function Home() {
  const navigate = useNavigate();

  useEffect(() => {
    fetch(`${process.env.REACT_APP_SERVER_URL}/auth/protected`, {
      credentials: "include",
    })
      .then((res) => {
        if (res.status !== 200) navigate("/login");
        return res.json();
      })
      .then((data) => console.log(data))
      .catch(() => startTransition(() => navigate("/login")));
  }, []);

  const handleLogout = () => {
    fetch(`${process.env.REACT_APP_SERVER_URL}/auth/logout`, {
      method: "POST",
      credentials: "include",
    })
      .then((res) => res.json())
      .then((data) => console.log(data))
      .catch((err) => console.error(err))
      .finally(() => navigate("/login"));
  };

  const handleProfileClick = () => {
    startTransition(() => {
      navigate("/profile");
    });
  };

  return (
    <>
      <button onClick={() => handleLogout()}>logout</button>
      <button onClick={() => handleProfileClick()}>profile</button>
      <div style={{ display: "flex" }}>
        <LeftBar />
        <MainSection />
        <RightBar />
      </div>
    </>
  );
}
