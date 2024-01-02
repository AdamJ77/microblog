import axios from "axios";
import { useEffect, useState } from "react";
import IPost from "../models/IPost";
import { preparePosts } from "../utils/preparePosts";
import { useInView } from "react-intersection-observer";

const prepareLink = (link: string): string => {
  const splitted = link.split("/");
  const last = splitted[splitted.length - 1];
  return `${process.env.REACT_APP_SERVER_URL}/${last}`;
};

export default function useFetchPosts() {
  const [hasMore, setHasMore] = useState(true);
  const { ref, inView } = useInView({
    rootMargin: "500px",
    threshold: 0,
  });
  const [link, setLink] = useState(
    `${process.env.REACT_APP_SERVER_URL}/posts/?start=0&count=3`
  );
  const [posts, setPosts] = useState<IPost[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPosts = () => {
      if (!inView) return;

      setIsLoading(true);
      axios
        .get(link)
        .then((response) => {
          console.log(response.data.data);
          if (response.status !== 200) throw new Error();
          if (response.data.data.length === 0) setHasMore(false);
          setLink(prepareLink(response.data.links.next));
          setPosts((prev) => [...prev, ...preparePosts(response.data)]);
        })
        .catch((err) => setError(err))
        .finally(() => setIsLoading(false));
    };

    fetchPosts();
  }, [link, inView]);

  return { posts, isLoading, error, ref, hasMore };
}
