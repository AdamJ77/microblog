export default interface IPost {
  id: string;
  body: string;
  media: string[];
  created: Date;
  author: {
    id: string;
    name: string;
    avatar: string;
  };
}
