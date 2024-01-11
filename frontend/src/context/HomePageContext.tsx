import React, { createContext, useContext } from "react";
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
