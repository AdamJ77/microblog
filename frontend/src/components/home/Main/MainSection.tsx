import React from "react";
import styles from "./styles/MainSection.module.css";
import Search from "./Search";
import PostUploader from "./PostUploader";
import Posts from "./Posts";
import PostsContextProvider from "../../../context/PostsProvider";

export default function MainSection() {
  return (
    <main className={styles.main}>
      <Search />
      <PostsContextProvider>
        <PostUploader />
        <Posts />
      </PostsContextProvider>
    </main>
  );
}
