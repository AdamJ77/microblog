import IPost from "../../../../../models/IPost";
import { preparePosts } from "../preparePosts";

describe("preparePosts", () => {
  const apiData = {
    links: {
      self: "http://microblog.com/posts?start=0&count=2",
      next: "http://microblog.com/posts?start=2&count=5",
    },
    data: [
      {
        id: "7",
        type: "posts",
        attributes: {
          author: {
            id: "213",
            attributes: {
              name: "Greg",
              avatar: {
                src: "https://bank.pl/wp-content/uploads/2022/06/jaroslaw-kaczynski-753x424-gov-pl.jpg",
              },
            },
          },
          body: `Szanowni Państwo,`,
          created: "2023-04-20T18:34:59.000Z",
          media: [],
        },
      },
      {
        id: "13",
        type: "posts",
        attributes: {
          author: {
            id: "411",
            attributes: {
              name: "Mediocrates",
              avatar: {
                src: "https://edceah5uf5z.exactdn.com/wp-content/uploads/2023/05/Donald-Tusk-2.jpg?strip=all&lossy=1&sharp=1&ssl=1",
              },
            },
          },
          body: "Eh... good enough",
          created: "2023-11-07T23:20:47.000Z",
          media: [
            {
              type: "image",
              src: "https://bi.im-g.pl/im/e1/4b/1c/z29670113AMP,Starship.jpg",
            },
            {
              type: "video",
              src: `https://microblog/videos/test.mp4`,
            },
          ],
        },
      },
    ],
  };

  const desiredFormat: IPost[] = [
    {
      id: "7",
      body: "Szanowni Państwo,",
      media: [],
      created: new Date("2023-04-20T18:34:59.000Z"),
      author: {
        id: "213",
        name: "Greg",
        avatar:
          "https://bank.pl/wp-content/uploads/2022/06/jaroslaw-kaczynski-753x424-gov-pl.jpg",
      },
    },
    {
      id: "13",
      body: "Eh... good enough",
      media: [
        "https://bi.im-g.pl/im/e1/4b/1c/z29670113AMP,Starship.jpg",
        `https://microblog/videos/test.mp4`,
      ],
      created: new Date("2023-11-07T23:20:47.000Z"),
      author: {
        id: "411",
        name: "Mediocrates",
        avatar:
          "https://edceah5uf5z.exactdn.com/wp-content/uploads/2023/05/Donald-Tusk-2.jpg?strip=all&lossy=1&sharp=1&ssl=1",
      },
    },
  ];

  it("correctly converts api response to IPost[]", () => {
    const formatted = preparePosts(apiData);
    expect(formatted).toEqual(desiredFormat);
  });
});
