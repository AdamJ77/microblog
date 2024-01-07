import IPost from "../models/IPost";

export const preparePosts = (apiResponse: any): IPost[] => {
  const data = apiResponse.data;

  const posts: IPost[] = data.map((single: any) => {
    const id = single.id;
    const { body, created, media } = single.attributes;
    const author = single.attributes.author;
    const authorID = author.id;
    const authorName = author.attributes.name;
    const authorAvatar = author.attributes.avatar.src;

    const mediaParsed = media.map((single: any) => single.src);

    const post = {
      id,
      body,
      media: mediaParsed,
      created: new Date(created),
      author: {
        id: authorID,
        name: authorName,
        avatar: authorAvatar,
      },
    } as IPost;

    return post;
  });

  return posts;
};
