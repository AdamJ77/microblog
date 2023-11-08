export default interface IPost {
  id: number;
  body: string;
  media: string[];
  created: Date;
  author: {
    id: number;
    name: string;
    avatar: string;
  };
}
