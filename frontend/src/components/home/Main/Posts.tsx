import React from "react";
import Post from "./Post";
import styles from "./styles/Posts.module.css";
import IPost from "../../../models/IPost";

export default function Posts() {
  const posts: IPost[] = [
    {
      id: 1,
      body: `Szanowni Państwo,

      Jestem Jarosław Kaczyński, politykiem o wieloletnim doświadczeniu w polskiej polityce. Chciałbym podzielić się kilkoma myślami związanymi z moją działalnością i przekonaniami.
      
      Od zawsze wierzę w suwerenność i niepodległość Polski. To przekonanie jest fundamentem mojego zaangażowania politycznego. Wraz z moją partią, Prawo i Sprawiedliwość (PiS), staramy się chronić naszą tożsamość narodową, nasze tradycje i wartości. Dążymy do tego, by Polska była silnym i niezależnym krajem na arenie międzynarodowej.
      
      Nasza polityka koncentruje się także na kwestiach społecznych i ekonomicznych. Chcemy, aby Polacy mieli godne życie, dostęp do opieki zdrowotnej i edukacji na najwyższym poziomie. Nasze reformy i programy społeczne miały na celu poprawę jakości życia obywateli.
      
      Oczywiście, moja działalność polityczna nie była pozbawiona kontrowersji. Rozumiem, że nasze decyzje nie zawsze były akceptowane przez wszystkich. Jednak zawsze staramy się działać z myślą o najlepszym interesie Polski.
      
      Dla mnie i dla mojej partii ważne jest także poszanowanie praworządności oraz niezależności sądownictwa. To fundament demokracji, który musi być chroniony.

      Mimo różnic w ocenach, niezmiennie pozostaję oddanym służbie Polsce i jej mieszkańcom. Dążę do tego, aby nasz kraj rozwijał się, był silny i suwerenny. Mam nadzieję, że nasza praca przyczynia się do tego celu.
      
      Z poważaniem,
      Jarosław Kaczyński`,
      media: [
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcnQzCTrdeR0SXikJ4ovPPcw6RNT0QU2OCSA&usqp=CAU",
      ],
      created: new Date(2023, 7, 24, 22, 13, 12),
      author: {
        id: 1,
        name: "Jarosław Kaczyński",
        avatar:
          "https://bank.pl/wp-content/uploads/2022/06/jaroslaw-kaczynski-753x424-gov-pl.jpg",
      },
    },
    {
      id: 2,
      body: `Hello,

      I'm Elon Musk, a business magnate, entrepreneur, and the CEO of several companies, including SpaceX and Tesla. I'd like to share a few thoughts with you.
      
      My mission in life has been to drive innovation and make a positive impact on the world. I'm deeply passionate about space exploration, sustainable energy, and the future of technology. Through SpaceX, I aim to make space travel more accessible and enable humanity to become a multi-planetary species. At Tesla, we're working towards a sustainable future by developing electric vehicles and renewable energy solutions.
      
      I believe in the power of entrepreneurship and the potential for individuals to shape the future. I encourage risk-taking, bold ideas, and a focus on solving some of the world's most pressing challenges.
      
      Of course, my ventures have had their share of controversies and hurdles, but I remain committed to pushing the boundaries of what's possible and improving our world.
      
      Thank you for being a part of this incredible journey, and together, let's make the future a better place.
      
      Best regards,
      Elon Musk`,
      media: [
        "https://v.wpimg.pl/YWJmNTVidjYrDzhneRJ7I2hXbD0_S3V1P090dnlYa296FWEyPwU8JS8dIXoxGywnKxo-eiYFdjY6BGEiZ0Y9PjkdIjUvRjw6KAgqezJZa2YuCS9he144Y3lAemJnDHRvK14veW8LaDYoC3thNF88ZWgQ",
        "https://bi.im-g.pl/im/e1/4b/1c/z29670113AMP,Starship.jpg",
        `${process.env.PUBLIC_URL}/videos/test.mp4`,
      ],
      created: new Date(2023, 9, 29, 22, 13, 12),
      author: {
        id: 1,
        name: "Elon Musk",
        avatar:
          "https://i.gremicdn.pl/image/free/2042e815ec347f2c640c04c12ac26941/?t=crop:1920:1191:nowe:0:86,resize:fill:408:255,enlarge:1",
      },
    },
    {
      id: 3,
      body: `Liebe Freunde,

      Ich bin Donald Tusk, ein polnischer Politiker, der das Privileg hatte, in verschiedenen Führungspositionen in der Europäischen Union und Polen tätig zu sein. Ich möchte einige Gedanken mit Ihnen teilen.
      
      Während meiner Karriere lag mein Hauptaugenmerk auf der Förderung der europäischen Einheit und Zusammenarbeit. Ich glaube, dass ein vereintes Europa besser in der Lage ist, den Herausforderungen unserer Zeit zu begegnen und zum Frieden, zur Stabilität und zum Wohlstand beizutragen. Meine Amtszeit als Präsident des Europäischen Rates ermöglichte es mir, an der Stärkung der Rolle der EU auf der globalen Bühne zu arbeiten und gemeinsame Lösungen für komplexe Probleme zu finden.
      
      Ich lege auch großen Wert auf demokratische Werte und Rechtsstaatlichkeit, sowohl in Polen als auch in der gesamten EU. Es ist entscheidend, dass unsere Gesellschaften diese Prinzipien hochhalten, um eine gerechte und transparente Regierungsführung sicherzustellen.
      
      Ich verstehe, dass mein politischer Werdegang nicht ohne Kontroversen war und meine Ansichten nicht immer allgemein akzeptiert wurden. Dennoch bleibt meine Hingabe an ein starkes und vereintes Europa unerschütterlich.
      
      Ich bin dankbar für die Gelegenheiten, die ich hatte, um zu dienen und einen positiven Einfluss auszuüben, und freue mich darauf, meine Arbeit für eine bessere Zukunft für alle fortzusetzen.
      
      Mit freundlichen Grüßen,
      Donald Tusk`,
      media: [
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRovt5jwnUTK9JIyYgW7MEQFpNQRJYW_BhRWQ&usqp=CAU",
        "https://ocdn.eu/images/pulscms/ZTQ7MDA_/2743ab3b-1103-4b72-b822-38d0994dc6ef.jpeg",
      ],
      created: new Date(2022, 10, 5, 22, 13, 12),
      author: {
        id: 1,
        name: "Donald Tusk",
        avatar:
          "https://edceah5uf5z.exactdn.com/wp-content/uploads/2023/05/Donald-Tusk-2.jpg?strip=all&lossy=1&sharp=1&ssl=1",
      },
    },
  ];

  return (
    <div className={styles.posts}>
      {posts.map((post, index) => (
        <Post key={index} post={post} />
      ))}
    </div>
  );
}
