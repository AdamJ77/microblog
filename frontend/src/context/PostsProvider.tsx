import React, { createContext, useContext } from "react";
import useFetchPosts from "../hooks/useFetchPosts";
import IPost from "../models/IPost";

interface PostsContextProps {
  children: React.ReactNode;
}

interface PostsContextValue {
  posts: IPost[];
  isLoading: boolean;
  error: any;
  ref: any;
  hasMore: boolean;
  addPost: Function;
}

const PostsContext = createContext<PostsContextValue>({} as PostsContextValue);

export const usePostsContext = () => useContext(PostsContext);

export const PostsContextProvider = ({ children }: PostsContextProps) => {
  const { posts, isLoading, error, ref, hasMore, addPost } = useFetchPosts();

  return (
    <PostsContext.Provider
      value={{
        posts,
        isLoading,
        error,
        ref,
        hasMore,
        addPost,
      }}
    >
      {children}
    </PostsContext.Provider>
  );
};

export default PostsContextProvider;
