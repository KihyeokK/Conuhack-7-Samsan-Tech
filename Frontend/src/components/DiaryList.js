import React, { useEffect, useState } from "react";
import styles from "./DiaryList.module.css";

import DiaryEntry from "./DiaryEntry";

const DiaryList = (props) => {
  const [diaryEntries, setDiaryEntries] = useState([]);
  const [isDiaryEntryAdded, setIsDiaryEntryAdded] = useState(false);

  const dummyDiaryEntriesData = [
    {
      id: "1",
      diary:
        "today I ate lunch at McGill. It was delicious. I hope the semester ends soon. When is the next spring break?",
      emotions: ["sad", "happy", "calm"],
      playlistUrl: "dafdsfdfasdfs",
    },
    {
      id: "2",
      diary:
        "aydyfyasdfdsfysadyfsdfdsyfasdfasf",
      emotions: ["calm"],
      playlistUrl: "dafdsfdfasdfs",
    },
    {
      id: "3",
      diary:
        "today I ate lunch at McGill. It was delicious. I hope the semester ends soon. When is the next spring break?",
      emotions: ["sad", "happy", "calm"],
      playlistUrl: "dafdsfdfasdfs",
    },
    {
      id: "4",
      diary:
        "today I ate lunch at McGill. It was delicious. I hope the semester ends soon. When is the next spring break?",
      emotions: ["sad", "happy", "calm"],
      playlistUrl: "dafdsfdfasdfs",
    },
  ];

  const diaryList = dummyDiaryEntriesData.map((diaryEntry) => (
    <DiaryEntry
      onClick={props.onClick}
      className={styles["diary-entry"]}
      key={diaryEntry.id}
      date="Sep 09, 2023"
      isLiked={true}
      diary={diaryEntry.diary}
      emotions={diaryEntry.emotions}
      playlistUrl={diaryEntry.playlistUrl}
    />
  ));
  const fetchDiaryEntries = (userId) => {
    //fetch from backend
    //use setMood
  };

  // useEffect(() => {
  //   //setDiaryEntries = axios.get
  //   //setIsDiaryEntryAdded(false);
  // }, [fetchDiaryEntries, isDiaryEntryAdded]);
  useEffect(() => {
    //setDiaryEntries = axios.get
    console.log("trying to fetch within useEffect in DiaryList component");
    fetch("http://127.0.0.1:8000/diaries/")
      .then((response) => console.log(response))
      .catch((err) => console.log(err));
    //setIsDiaryEntryAdded(false);
  });

  return <ul className={styles.scrollable}>{diaryList}</ul>;
};

export default DiaryList;
