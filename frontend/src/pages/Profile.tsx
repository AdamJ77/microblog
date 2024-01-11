import React from "react";
import useFetch from "../hooks/useFetch";
import Loading from "../components/common/Loading";

export default function Profile() {
  const { data, isLoading } = useFetch(
    `${process.env.REACT_APP_SERVER_URL}/auth/user`,
    {
      withCredentials: true,
    }
  );

  if (isLoading) return <Loading text="" />;

  return <div>{JSON.stringify(data)}</div>;
}
