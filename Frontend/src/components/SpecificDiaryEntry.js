import CardForSpecificDiary from './UI/CardForSpecificDiary';
import styles from './SpecificDiaryEntry.module.css';
import logo from "./resources/images/Musical_Notes.png";

const SpecificDiaryEntry = (props) => {
    console.log(props.diary);
  return (
    <CardForSpecificDiary className={styles.cardDiary}>
      <h3 className={styles.date}>{new Date(props.diary.created_at).toDateString()}</h3>
      <p className={styles.diary}>{props.diary.content}</p>
      <div className={styles.emotions}>Analyzed emotion: {props.diary.mood}</div>
      <a className={styles.link} href={props.diary.music} target="_blank"><img className={styles.expandLogo} src={logo} alt="Logo" /></a>
    </CardForSpecificDiary>
  );
};

export default SpecificDiaryEntry;