import CardForSpecificDiary from './UI/CardForSpecificDiary';
import styles from './SpecificDiaryEntry.module.css';
import logo from "./resources/images/Musical_Notes.png";

const SpecificDiaryEntry = (props) => {
    console.log(props.diary);
  return (
    <CardForSpecificDiary className={styles.cardDiary}>
      <h3 className={styles.date}>{props.diary.date}</h3>
      <p className={styles.diary}>{props.diary.diary}</p>
      <div className={styles.emotions}>Analyzed emotion: {props.diary.emotions}</div>
      <a className={styles.link} href={props.diary.playlistUrl} target="_blank"><img className={styles.expandLogo} src={logo} alt="Logo" /></a>
    </CardForSpecificDiary>
  );
};

export default SpecificDiaryEntry;
