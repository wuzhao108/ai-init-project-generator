package {{ config.package }}.common;

{% if config.tech_stack.doc %}
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
{% endif %}

import java.io.Serializable;
import java.util.List;

/**
 * 分页查询结果
 * 
 * @author {{ config.name }}
 * @since 2024-01-01
 */
{% if config.tech_stack.doc %}
@ApiModel(description = "分页查询结果")
{% endif %}
public class PageResult<T> implements Serializable {

    private static final long serialVersionUID = 1L;

    /**
     * 当前页码
     */
    {% if config.tech_stack.doc %}
    @ApiModelProperty(value = "当前页码", example = "1")
    {% endif %}
    private Integer pageNum;

    /**
     * 每页大小
     */
    {% if config.tech_stack.doc %}
    @ApiModelProperty(value = "每页大小", example = "10")
    {% endif %}
    private Integer pageSize;

    /**
     * 总记录数
     */
    {% if config.tech_stack.doc %}
    @ApiModelProperty(value = "总记录数", example = "100")
    {% endif %}
    private Long total;

    /**
     * 总页数
     */
    {% if config.tech_stack.doc %}
    @ApiModelProperty(value = "总页数", example = "10")
    {% endif %}
    private Integer pages;

    /**
     * 数据列表
     */
    {% if config.tech_stack.doc %}
    @ApiModelProperty(value = "数据列表")
    {% endif %}
    private List<T> list;

    /**
     * 是否有上一页
     */
    {% if config.tech_stack.doc %}
    @ApiModelProperty(value = "是否有上一页", example = "false")
    {% endif %}
    private Boolean hasPrevious;

    /**
     * 是否有下一页
     */
    {% if config.tech_stack.doc %}
    @ApiModelProperty(value = "是否有下一页", example = "true")
    {% endif %}
    private Boolean hasNext;

    /**
     * 是否为第一页
     */
    {% if config.tech_stack.doc %}
    @ApiModelProperty(value = "是否为第一页", example = "true")
    {% endif %}
    private Boolean isFirst;

    /**
     * 是否为最后一页
     */
    {% if config.tech_stack.doc %}
    @ApiModelProperty(value = "是否为最后一页", example = "false")
    {% endif %}
    private Boolean isLast;

    /**
     * 构造函数
     */
    public PageResult() {
    }

    /**
     * 构造函数
     * 
     * @param pageNum 页码
     * @param pageSize 每页大小
     * @param total 总记录数
     * @param list 数据列表
     */
    public PageResult(Integer pageNum, Integer pageSize, Long total, List<T> list) {
        this.pageNum = pageNum;
        this.pageSize = pageSize;
        this.total = total;
        this.list = list;
        this.pages = (int) Math.ceil((double) total / pageSize);
        this.hasPrevious = pageNum > 1;
        this.hasNext = pageNum < pages;
        this.isFirst = pageNum == 1;
        this.isLast = pageNum.equals(pages);
    }

    /**
     * 创建分页结果
     * 
     * @param pageRequest 分页请求
     * @param total 总记录数
     * @param list 数据列表
     * @param <T> 数据类型
     * @return 分页结果
     */
    public static <T> PageResult<T> of(PageRequest pageRequest, Long total, List<T> list) {
        return new PageResult<>(pageRequest.getPageNum(), pageRequest.getPageSize(), total, list);
    }

    /**
     * 创建空的分页结果
     * 
     * @param pageRequest 分页请求
     * @param <T> 数据类型
     * @return 分页结果
     */
    public static <T> PageResult<T> empty(PageRequest pageRequest) {
        return new PageResult<>(pageRequest.getPageNum(), pageRequest.getPageSize(), 0L, null);
    }

    /**
     * 获取当前页码
     * 
     * @return 当前页码
     */
    public Integer getPageNum() {
        return pageNum;
    }

    /**
     * 设置当前页码
     * 
     * @param pageNum 当前页码
     */
    public void setPageNum(Integer pageNum) {
        this.pageNum = pageNum;
    }

    /**
     * 获取每页大小
     * 
     * @return 每页大小
     */
    public Integer getPageSize() {
        return pageSize;
    }

    /**
     * 设置每页大小
     * 
     * @param pageSize 每页大小
     */
    public void setPageSize(Integer pageSize) {
        this.pageSize = pageSize;
    }

    /**
     * 获取总记录数
     * 
     * @return 总记录数
     */
    public Long getTotal() {
        return total;
    }

    /**
     * 设置总记录数
     * 
     * @param total 总记录数
     */
    public void setTotal(Long total) {
        this.total = total;
        if (pageSize != null && pageSize > 0) {
            this.pages = (int) Math.ceil((double) total / pageSize);
        }
    }

    /**
     * 获取总页数
     * 
     * @return 总页数
     */
    public Integer getPages() {
        return pages;
    }

    /**
     * 设置总页数
     * 
     * @param pages 总页数
     */
    public void setPages(Integer pages) {
        this.pages = pages;
    }

    /**
     * 获取数据列表
     * 
     * @return 数据列表
     */
    public List<T> getList() {
        return list;
    }

    /**
     * 设置数据列表
     * 
     * @param list 数据列表
     */
    public void setList(List<T> list) {
        this.list = list;
    }

    /**
     * 是否有上一页
     * 
     * @return 是否有上一页
     */
    public Boolean getHasPrevious() {
        return hasPrevious;
    }

    /**
     * 设置是否有上一页
     * 
     * @param hasPrevious 是否有上一页
     */
    public void setHasPrevious(Boolean hasPrevious) {
        this.hasPrevious = hasPrevious;
    }

    /**
     * 是否有下一页
     * 
     * @return 是否有下一页
     */
    public Boolean getHasNext() {
        return hasNext;
    }

    /**
     * 设置是否有下一页
     * 
     * @param hasNext 是否有下一页
     */
    public void setHasNext(Boolean hasNext) {
        this.hasNext = hasNext;
    }

    /**
     * 是否为第一页
     * 
     * @return 是否为第一页
     */
    public Boolean getIsFirst() {
        return isFirst;
    }

    /**
     * 设置是否为第一页
     * 
     * @param isFirst 是否为第一页
     */
    public void setIsFirst(Boolean isFirst) {
        this.isFirst = isFirst;
    }

    /**
     * 是否为最后一页
     * 
     * @return 是否为最后一页
     */
    public Boolean getIsLast() {
        return isLast;
    }

    /**
     * 设置是否为最后一页
     * 
     * @param isLast 是否为最后一页
     */
    public void setIsLast(Boolean isLast) {
        this.isLast = isLast;
    }

    @Override
    public String toString() {
        return "PageResult{" +
                "pageNum=" + pageNum +
                ", pageSize=" + pageSize +
                ", total=" + total +
                ", pages=" + pages +
                ", list=" + list +
                ", hasPrevious=" + hasPrevious +
                ", hasNext=" + hasNext +
                ", isFirst=" + isFirst +
                ", isLast=" + isLast +
                '}';
    }
}