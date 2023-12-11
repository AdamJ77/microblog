import React from "react";
import styles from "./styles/LoginForm.module.css";
import { useNavigate } from "react-router-dom";

export default function LoginForm() {
  const navigate = useNavigate();

  const redirect = (event: React.MouseEvent<HTMLAnchorElement, MouseEvent>) => {
    event.preventDefault();
    navigate("/signup");
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const formData = new FormData(e.currentTarget);
    formData.forEach((val, key) => {
      console.log(key, val);
    });

    fetch(`${process.env.REACT_APP_SERVER_URL}/login`, {
      method: "POST",
      body: formData,
    }).then((res) => {
      if (res.status === 200) navigate("/");
    });

    // simulation of logging in
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
