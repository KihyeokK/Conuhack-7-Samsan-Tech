import styles from "./CardForSpecificDiary.module.css";

const CardForSpecificDiary = props => {
    return <div className={styles.card}>{props.children}</div>
}

export default CardForSpecificDiary;