import React, { useEffect, useState } from "react";
import Post from "./Post";
import styles from "./styles/Posts.module.css";
import { preparePosts } from "./utils/preparePosts";
import { apiData } from "./utils/apiData";
import IPost from "../../../models/IPost";
import { useInView } from "react-intersection-observer";

export default function Posts() {
  const [posts, setPosts] = useState<IPost[]>([]);
  const { ref, inView } = useInView({ rootMargin: "1000px" });

  useEffect(() => {
    if (!inView) return;

    setPosts((prev) => [...prev, ...preparePosts(apiData)]);
  }, [inView]);

  return (
    <div className={styles.posts}>
      {posts.map((post, index) => (
        <Post key={index} post={post} />
      ))}
      <div ref={ref} />
    </div>
  );
}
