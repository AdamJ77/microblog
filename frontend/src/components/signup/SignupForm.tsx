import React, { useState } from "react";
import { AVAILABLE_IMAGE_EXTENSIONS, DEFAULT_AVATAR } from "../../constants";
import styles from "./style/SignupForm.module.css";
import { useNavigate } from "react-router-dom";
import axios from "axios";

export default function SignupForm() {
  const [avatar, setAvatar] = useState(DEFAULT_AVATAR);
  const [form, setForm] = useState({
    login: "",
    password: "",
    confirmPassword: "",
    avatar: "",
  });
  const navigate = useNavigate();

  const handleAvatarChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files && e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      const photoPreview = event.target?.result as string;
      setAvatar(photoPreview);
    };
    reader.readAsDataURL(file);

    handleFormChange(e);
  };

  const handleAvatarRemove = (
    e: React.MouseEvent<HTMLButtonElement, MouseEvent>
  ) => {
    e.preventDefault();
    const input = document.getElementById("signup-image") as HTMLInputElement;
    input.value = "";
    setAvatar(DEFAULT_AVATAR);

    setForm((prev) => ({ ...prev, avatar: "" }));
  };

  const redirect = (e: React.MouseEvent<HTMLAnchorElement, MouseEvent>) => {
    e.preventDefault();
    navigate("/login");
  };

  const acceptedImages = AVAILABLE_IMAGE_EXTENSIONS.map(
    (ext) => "." + ext
  ).join(", ");

  const handleFormChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm((prev) => ({
      ...prev,
      [e.target.name]: e.target.files ? e.target.files : e.target.value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const isValidPassword = form.password === form.confirmPassword;

    if (!isValidPassword) alert("Passwords don't match.");

    const formData = new FormData(e.currentTarget);

    const body = {
      login: formData.get("login"),
      password: formData.get("password"),
      avatar: "http://avatar.com/ufgyuerwgfyur",
    };

    try {
      const data = await axios.post(
        `${process.env.REACT_APP_SERVER_URL}/auth/signup`,
        body
      );
      if (data.status !== 200) throw new Error();
      console.log(data);
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <h2 className={styles.h2}>Signup</h2>
      <div style={{ display: "flex", width: "100%" }}>
        <div style={{ position: "relative", width: "40%", marginTop: "50px" }}>
          <img src={avatar} alt="avatar" className={styles.avatar} />
          {avatar !== DEFAULT_AVATAR && (
            <button
              onClick={handleAvatarRemove}
              className={styles["remove-avatar"]}
            >
              <img
                src={`${process.env.PUBLIC_URL}/icons/remove_avatar.svg`}
                alt="remove avatar"
              />
            </button>
          )}
          <br />
          <label
            htmlFor="signup-image"
            className={styles["change-avatar-label"]}
          >
            change avatar
          </label>
          <input
            type="file"
            name="avatar"
            id="signup-image"
            accept={acceptedImages}
            style={{ display: "none" }}
            onChange={handleAvatarChange}
          />
        </div>
        <div style={{ width: "60%" }}>
          <input
            type="text"
            name="login"
            placeholder="login"
            className={styles.input}
            required
            onChange={handleFormChange}
          />
          <input
            type="password"
            name="password"
            placeholder="password"
            className={styles.input}
            required
            onChange={handleFormChange}
          />
          <input
            type="password"
            name="confirmPassword"
            placeholder="confirm password"
            className={styles.input}
            required
            onChange={handleFormChange}
          />
        </div>
      </div>
      <button type="submit" className={styles.button}>
        signup
      </button>
      <p className={styles.p}>
        Already have account? Log in{" "}
        <a onClick={redirect} href="/login">
          here
        </a>
        .
      </p>
    </form>
  );
}
