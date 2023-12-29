import React from "react";
import styles from "./styles/LoginForm.module.css";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useAppContext } from "../../context/AppContext";

export default function LoginForm() {
  const { tokenRef } = useAppContext();
  const navigate = useNavigate();

  const redirect = (event: React.MouseEvent<HTMLAnchorElement, MouseEvent>) => {
    event.preventDefault();
    navigate("/signup");
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const formData = new FormData(e.currentTarget);

    const body = {
      login: formData.get("login"),
      password: formData.get("password"),
    };

    try {
      const data = await axios.post(
        `${process.env.REACT_APP_SERVER_URL}/auth/login`,
        body
      );

      tokenRef.current = data.data.token;
    } catch (e) {
      return;
    }

    navigate("/");
  };

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <h2 className={styles.h2}>login</h2>
      <input
        type="text"
        required
        name="login"
        placeholder="login"
        className={styles.input}
      />
      <input
        type="password"
        required
        name="password"
        placeholder="password"
        className={styles.input}
      />
      <button type="submit" className={styles.button}>
        login
      </button>
      <p className={styles.p}>
        Don't have account? Sign up{" "}
        <a onClick={redirect} href="/signup">
          here
        </a>
        .
      </p>
    </form>
  );
}
