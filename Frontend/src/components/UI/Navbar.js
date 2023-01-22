import styles from "./Navbar.module.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHeart, faChevronRight } from "@fortawesome/free-solid-svg-icons";
import { useState } from "react";
import logo from "../resources/images/Double_Up.png";
import heart from "../resources/images/Heart.png";
import mask from "../resources/images/Theatre_Mask.png";
import userLogo from "../resources/images/User.png";
import music from "../resources/images/Musical_Notes.png";
import mainLogo from "../resources/images/mainLogo.png"

const Navbar = (props) => {
  const [isNavbarExpanded, setIsNavBarExpanded] = useState(false);

  const onExpandClickHandler = () => {
    setIsNavBarExpanded(true);
  };

  return (
    <nav className={styles.nav}>
      <ul className={styles["navbar-nav"]}>
        {/* <li className={isNavbarExpanded ? styles['nav-item'] : ''}> */}
        <li className={styles["nav-item-main-logo"]}>
          {/* use Link tag  */}
          <a href="#" className={styles["nav-link"]}>
          <img className={styles.centralLogo} src={mainLogo} alt="Logo" />
          </a>
        </li>
        <li className={styles["nav-item-login"]}>
          {/* use Link tag  */}
          <a href="#" className={styles["nav-link"]}>
          login
          </a>
        </li>
        <li className={styles["nav-item"]}>
          {/* use Link tag  */}
          <a href="#" className={styles["nav-link"]}>
          <img className={styles.centralLogo} src={mask} alt="Logo" />
            <span className={styles["link-text"]}>my entries</span>
          </a>
        </li>
        <li className={styles["nav-item"]}>
          {/* use Link tag  */}
          <a href="#" className={styles["nav-link"]}>
            <img className={styles.centralLogo} src={heart} alt="Logo" />
            <span className={styles["link-text"]}>my hearts</span>
          </a>
        </li>
        <li className={styles["nav-item"]}>
          {/* use Link tag  */}
          <a href="#" className={styles["nav-link"]}>
            <img className={styles.centralLogo} src={music} alt="Logo" />
            <span className={styles["link-text"]}>my music</span>
          </a>
        </li>
        <li className={styles["nav-item"]}>
          {/* use Link tag  */}
          <a href="#" className={styles["nav-link"]}>
            <img className={styles.centralLogo} src={userLogo} alt="Logo" />
            <span className={styles["link-text"]}>my profile</span>
          </a>
        </li>
        <li className={styles["nav-item-arrow"]}>
          {/* use Link tag  */}
          <button onClick={onExpandClickHandler}>
            {/* <FontAwesomeIcon icon={faChevronRight} /> */}
            <img className={styles.expandLogo} src={logo} alt="Logo" />
          </button>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
