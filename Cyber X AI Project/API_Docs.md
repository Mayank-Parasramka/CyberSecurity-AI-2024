## API Documentation:

Below is the default generated API Documentation in json format, that can be compiled in Swagger Editor.

```
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
paths:
  /register:
    post:
      summary: Register User
      operationId: register_user_register_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserCreate'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
  /token:
    post:
      summary: Login For Access Token
      operationId: login_for_access_token_token_post
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Body_login_for_access_token_token_post'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
  /verify-token/{token}:
    get:
      summary: Verify User Token
      operationId: verify_user_token_verify_token__token__get
      parameters:
        - name: token
          in: path
          required: true
          schema:
            type: string
            title: Token
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
  /upload-pos-logs/:
    post:
      summary: Upload Pos Logs
      operationId: upload_pos_logs_upload_pos_logs__post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RequestLog'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - OAuth2PasswordBearer: []
  /get-last-pos-logs/:
    get:
      summary: Get Last Pos Logs
      operationId: get_last_pos_logs_get_last_pos_logs__get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
      security:
        - OAuth2PasswordBearer: []
  /get-pos-log-stats/:
    get:
      summary: Get Pos Log Stats
      operationId: get_pos_log_stats_get_pos_log_stats__get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
      security:
        - OAuth2PasswordBearer: []
components:
  schemas:
    Body_login_for_access_token_token_post:
      properties:
        grant_type:
          anyOf:
            - type: string
              pattern: password
            - type: 'null'
          title: Grant Type
        username:
          type: string
          title: Username
        password:
          type: string
          title: Password
        scope:
          type: string
          title: Scope
          default: ''
        client_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Client Id
        client_secret:
          anyOf:
            - type: string
            - type: 'null'
          title: Client Secret
      type: object
      required:
        - username
        - password
      title: Body_login_for_access_token_token_post
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    RequestLog:
      properties:
        new_pos:
          type: string
          title: New Pos
      type: object
      required:
        - new_pos
      title: RequestLog
    UserCreate:
      properties:
        username:
          type: string
          title: Username
        password:
          type: string
          title: Password
      type: object
      required:
        - username
        - password
      title: UserCreate
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
  securitySchemes:
    OAuth2PasswordBearer:
      type: oauth2
      flows:
        password:
          scopes: {}
          tokenUrl: token
```
