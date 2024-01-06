export default interface IPost {
  id: string;
  body: string;
  media: string[];
  created: Date;
  author: {
    id: number;
    name: string;
    avatar: string;
  };
}
