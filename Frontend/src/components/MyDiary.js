import DiaryList from "./DiaryList";
import DiaryForm from "./DiaryForm";
import SpecificDiaryEntry from "./SpecificDiaryEntry";
import Navbar from "./UI/Navbar";
import styles from './MyDiary.module.css';
import { useState, useEffect } from "react";

const MyDiary = (props) => {
  const [clickedDiaryEntry, setClickedDiaryEntry] = useState(null);
  const [isFethced, setIsFetched] = useState(false);

  const diaryClickHandler = (diaryEntry) => {
    setClickedDiaryEntry(diaryEntry);
    console.log(clickedDiaryEntry);
  }

  const fetchHandler = (returnedDiary) => {
    setIsFetched(true);
    setClickedDiaryEntry(returnedDiary);
    console.log(isFethced);
  }

  return (
    <>
      <Navbar />
      <main className={styles["main-diary"]}>
        <DiaryList isFetched={isFethced} onClick={diaryClickHandler}/>
        {clickedDiaryEntry ? <SpecificDiaryEntry diary={clickedDiaryEntry} /> : <DiaryForm onFetched={fetchHandler} />}
      </main>
    </>
  );
};

export default MyDiary;
