import React, { createContext, useContext, useEffect } from "react";
import axios from "axios";
import useFetch from "../hooks/useFetch";

interface HomePageContextProps {
  children: React.ReactNode;
}

interface HomePageContextValue {
  user: IUser | null;
  isLoading: boolean;
  error: any;
}

const HomePageContext = createContext<HomePageContextValue>(
  {} as HomePageContextValue
);

export const useHomePageContext = () => useContext(HomePageContext);

export const HomePageContextProvider = ({ children }: HomePageContextProps) => {
  const { data, isLoading, error } = useFetch<IUser>(
    `${process.env.REACT_APP_SERVER_URL}/auth/user`,
    {
      withCredentials: true,
    }
  );

  useEffect(() => {
    console.log(data);
  }, [data]);

  return (
    <HomePageContext.Provider
      value={{
        user: data,
        isLoading,
        error,
      }}
    >
      {children}
    </HomePageContext.Provider>
  );
};

export default HomePageContextProvider;
