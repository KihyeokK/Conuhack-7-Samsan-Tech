const DiaryEntry = props => {
    return <li className={props.className}>
        my mood on <span>{props.date}</span><span>{props.isLiked}</span>
    </li>
}

export default DiaryEntry;