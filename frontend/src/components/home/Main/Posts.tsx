import React from "react";
import Post from "./Post";
import styles from "./styles/Posts.module.css";
import { preparePosts } from "./utils/preparePosts";

export default function Posts() {
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
          body: `Szanowni Państwo,
    Jestem Jarosław Kaczyński, politykiem o wieloletnim doświadczeniu w polskiej polityce. Chciałbym podzielić się kilkoma myślami związanymi z moją działalnością i przekonaniami.
    Od zawsze wierzę w suwerenność i niepodległość Polski. To przekonanie jest fundamentem mojego zaangażowania politycznego. Wraz z moją partią, Prawo i Sprawiedliwość (PiS), staramy się chronić naszą tożsamość narodową, nasze tradycje i wartości. Dążymy do tego, by Polska była silnym i niezależnym krajem na arenie międzynarodowej.
    Nasza polityka koncentruje się także na kwestiach społecznych i ekonomicznych. Chcemy, aby Polacy mieli godne życie, dostęp do opieki zdrowotnej i edukacji na najwyższym poziomie. Nasze reformy i programy społeczne miały na celu poprawę jakości życia obywateli.
    Oczywiście, moja działalność polityczna nie była pozbawiona kontrowersji. Rozumiem, że nasze decyzje nie zawsze były akceptowane przez wszystkich. Jednak zawsze staramy się działać z myślą o najlepszym interesie Polski.
    Dla mnie i dla mojej partii ważne jest także poszanowanie praworządności oraz niezależności sądownictwa. To fundament demokracji, który musi być chroniony.
    Mimo różnic w ocenach, niezmiennie pozostaję oddanym służbie Polsce i jej mieszkańcom. Dążę do tego, aby nasz kraj rozwijał się, był silny i suwerenny. Mam nadzieję, że nasza praca przyczynia się do tego celu.
    Z poważaniem,
        Jarosław Kaczyński`,
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
              src: `${process.env.PUBLIC_URL}/videos/test.mp4`,
            },
          ],
        },
      },
      {
        id: "13",
        type: "posts",
        attributes: {
          author: {
            id: "411",
            attributes: {
              name: "Elon",
              avatar: {
                src: "https://i.gremicdn.pl/image/free/2042e815ec347f2c640c04c12ac26941/?t=crop:1920:1191:nowe:0:86,resize:fill:408:255,enlarge:1",
              },
            },
          },
          body: "Short post",
          created: "2023-11-23T23:20:47.000Z",
          media: [],
        },
      },
    ],
  };

  const posts = preparePosts(apiData);

  return (
    <div className={styles.posts}>
      {posts.map((post, index) => (
        <Post key={index} post={post} />
      ))}
    </div>
  );
}
