# Security Policy

## 1. Authentication

- JWT (JSON Web Token) based authentication
- OAuth2 Password flow
- Bearer token required for protected routes
- Token contains user email (sub)

---

## 2. Authorization

Role-based access control:

- Only DOCTOR can:
  - Create slots
  - Create consultations
  - Create prescriptions

- Only PATIENT can:
  - Book slots

Unauthorized access returns 403 Forbidden.

---

## 3. Password Security

- Passwords are hashed before storing in database
- Plain passwords are never stored
- Password verification done using hashing algorithm

---

## 4. Token Security

- Tokens are signed using SECRET_KEY
- Algorithm: HS256
- Invalid or tampered tokens are rejected

---

## 5. Input Validation

- Pydantic schemas used for validation
- Prevents malformed JSON input
- Ensures required fields are present

---

## 6. Logging & Monitoring

- All critical actions logged
- Unauthorized attempts logged
- Helps detect suspicious behavior

---

## 7. Future Improvements

For production:

- Use HTTPS only
- Add refresh tokens
- Implement rate limiting
- Add account lockout mechanism
- Use secure environment variables
- Rotate SECRET_KEY periodically
