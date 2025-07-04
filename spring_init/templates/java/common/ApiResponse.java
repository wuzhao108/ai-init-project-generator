package {{ config.package }}.common;

import java.io.Serializable;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

{% if 'swagger' in config.tech_stack.docs %}
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
{% endif %}

/**
 * 统一API响应结构
 * 
 * @author {{ config.name }}
 * @since {{ "now" | strftime("%Y-%m-%d") }}
 */
{% if 'swagger' in config.tech_stack.docs %}
@ApiModel(description = "统一API响应结构")
{% endif %}
public class ApiResponse<T> implements Serializable {

    private static final long serialVersionUID = 1L;

    /**
     * 成功状态码
     */
    public static final int SUCCESS_CODE = 200;

    /**
     * 失败状态码
     */
    public static final int ERROR_CODE = 500;

    /**
     * 未授权状态码
     */
    public static final int UNAUTHORIZED_CODE = 401;

    /**
     * 禁止访问状态码
     */
    public static final int FORBIDDEN_CODE = 403;

    /**
     * 资源不存在状态码
     */
    public static final int NOT_FOUND_CODE = 404;

    /**
     * 参数错误状态码
     */
    public static final int PARAM_ERROR_CODE = 400;

    /**
     * 状态码
     */
    {% if 'swagger' in config.tech_stack.docs %}
    @ApiModelProperty(value = "状态码", example = "200")
    {% endif %}
    private int code;

    /**
     * 响应消息
     */
    {% if 'swagger' in config.tech_stack.docs %}
    @ApiModelProperty(value = "响应消息", example = "操作成功")
    {% endif %}
    private String message;

    /**
     * 响应数据
     */
    {% if 'swagger' in config.tech_stack.docs %}
    @ApiModelProperty(value = "响应数据")
    {% endif %}
    private T data;

    /**
     * 时间戳
     */
    {% if 'swagger' in config.tech_stack.docs %}
    @ApiModelProperty(value = "时间戳", example = "2023-01-01 12:00:00")
    {% endif %}
    private String timestamp;

    /**
     * 是否成功
     */
    {% if 'swagger' in config.tech_stack.docs %}
    @ApiModelProperty(value = "是否成功", example = "true")
    {% endif %}
    private boolean success;

    /**
     * 构造函数
     */
    public ApiResponse() {
        this.timestamp = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
    }

    /**
     * 构造函数
     * 
     * @param code 状态码
     * @param message 响应消息
     * @param data 响应数据
     */
    public ApiResponse(int code, String message, T data) {
        this.code = code;
        this.message = message;
        this.data = data;
        this.success = code == SUCCESS_CODE;
        this.timestamp = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
    }

    /**
     * 成功响应
     * 
     * @param <T> 数据类型
     * @return API响应
     */
    public static <T> ApiResponse<T> success() {
        return new ApiResponse<>(SUCCESS_CODE, "操作成功", null);
    }

    /**
     * 成功响应
     * 
     * @param message 响应消息
     * @param <T> 数据类型
     * @return API响应
     */
    public static <T> ApiResponse<T> success(String message) {
        return new ApiResponse<>(SUCCESS_CODE, message, null);
    }

    /**
     * 成功响应
     * 
     * @param data 响应数据
     * @param <T> 数据类型
     * @return API响应
     */
    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>(SUCCESS_CODE, "操作成功", data);
    }

    /**
     * 成功响应
     * 
     * @param message 响应消息
     * @param data 响应数据
     * @param <T> 数据类型
     * @return API响应
     */
    public static <T> ApiResponse<T> success(String message, T data) {
        return new ApiResponse<>(SUCCESS_CODE, message, data);
    }

    /**
     * 失败响应
     * 
     * @param <T> 数据类型
     * @return API响应
     */
    public static <T> ApiResponse<T> error() {
        return new ApiResponse<>(ERROR_CODE, "操作失败", null);
    }

    /**
     * 失败响应
     * 
     * @param message 响应消息
     * @param <T> 数据类型
     * @return API响应
     */
    public static <T> ApiResponse<T> error(String message) {
        return new ApiResponse<>(ERROR_CODE, message, null);
    }

    /**
     * 失败响应
     * 
     * @param code 状态码
     * @param message 响应消息
     * @param <T> 数据类型
     * @return API响应
     */
    public static <T> ApiResponse<T> error(int code, String message) {
        return new ApiResponse<>(code, message, null);
    }

    /**
     * 参数错误响应
     * 
     * @param message 响应消息
     * @param <T> 数据类型
     * @return API响应
     */
    public static <T> ApiResponse<T> paramError(String message) {
        return new ApiResponse<>(PARAM_ERROR_CODE, message, null);
    }

    /**
     * 未授权响应
     * 
     * @param <T> 数据类型
     * @return API响应
     */
    public static <T> ApiResponse<T> unauthorized() {
        return new ApiResponse<>(UNAUTHORIZED_CODE, "未授权", null);
    }

    /**
     * 禁止访问响应
     * 
     * @param <T> 数据类型
     * @return API响应
     */
    public static <T> ApiResponse<T> forbidden() {
        return new ApiResponse<>(FORBIDDEN_CODE, "禁止访问", null);
    }

    /**
     * 资源不存在响应
     * 
     * @param <T> 数据类型
     * @return API响应
     */
    public static <T> ApiResponse<T> notFound() {
        return new ApiResponse<>(NOT_FOUND_CODE, "资源不存在", null);
    }

    /**
     * 资源不存在响应
     * 
     * @param message 响应消息
     * @param <T> 数据类型
     * @return API响应
     */
    public static <T> ApiResponse<T> notFound(String message) {
        return new ApiResponse<>(NOT_FOUND_CODE, message, null);
    }

    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }

    public boolean isSuccess() {
        return success;
    }

    public void setSuccess(boolean success) {
        this.success = success;
    }

    @Override
    public String toString() {
        return "ApiResponse{" +
                "code=" + code +
                ", message='" + message + '\'' +
                ", data=" + data +
                ", timestamp='" + timestamp + '\'' +
                ", success=" + success +
                '}';
    }
}