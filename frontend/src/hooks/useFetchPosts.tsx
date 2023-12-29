import axios from "axios";
import { useEffect, useState } from "react";
import IPost from "../models/IPost";
import { preparePosts } from "../utils/preparePosts";

export default function useFetchPosts() {
  const [link, setLink] = useState(
    `${process.env.REACT_APP_SERVER_URL}/posts/?start=0&count=1`
  );
  const [posts, setPosts] = useState<IPost[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    setIsLoading(true);
    axios
      .get(link)
      .then((response) => {
        if (response.status !== 200) throw new Error();
        setLink(response.data.links.next);
        setPosts((prev) => [...prev, ...preparePosts(response.data)]);
      })
      .catch((err) => setError(err))
      .finally(() => setIsLoading(false));
  }, []);

  return { posts, isLoading, error };
}
