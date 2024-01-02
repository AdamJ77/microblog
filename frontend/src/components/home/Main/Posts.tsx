import React from "react";
import Post from "./Post";
import styles from "./styles/Posts.module.css";
import useFetchPosts from "../../../hooks/useFetchPosts";

export default function Posts() {
  const { posts, isLoading, ref, hasMore } = useFetchPosts();

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
