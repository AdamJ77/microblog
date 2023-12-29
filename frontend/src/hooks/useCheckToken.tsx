import React, { useEffect } from "react";
import { useAppContext } from "../context/AppContext";
import { useNavigate } from "react-router-dom";

export default function useCheckToken() {
  const { tokenRef } = useAppContext();
  const navigate = useNavigate();

  useEffect(() => {
    if (!tokenRef.current) navigate("/login");
  }, []);
}
