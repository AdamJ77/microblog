import React from "react";
import Post from "./Post";
import styles from "./styles/Posts.module.css";
import { usePostsContext } from "../../../context/PostsProvider";

export default function Posts() {
  const { posts, isLoading, ref, hasMore } = usePostsContext();

  if (isLoading) return <div>loading...</div>;

  return (
    <div className={styles.posts}>
      {posts.map((post, index) => (
        <Post key={index} post={post} />
      ))}
      {hasMore && <div ref={ref} />}
    </div>
  );
}
